#!/bin/bash

MAX_ITERATIONS=$(awk -F'=' '/MAX_ITERATIONS/ {gsub(/[[:space:]]/, "", $2); print $2}' ../peter/config.py)
MAX_EXECUTIONS=$(awk -F'=' '/MAX_EXECUTIONS/ {gsub(/[[:space:]]/, "", $2); print $2}' ../peter/config.py)

# Parameters
hypotheses=(peter common)
strategies=(best worst random)

for hypothesis in "${hypotheses[@]}"; do
  cd $hypothesis
  for strategy in "${strategies[@]}"; do
    cd $strategy
    
    mean_file=$hypothesis"_"$strategy"_mean.csv"
    
    [ -e "$mean_file" ] && rm "$mean_file"
    
    for ((iteration=0; iteration<MAX_ITERATIONS; iteration++)); do
      sum=0
      count=0

      for ((i=0; i<MAX_EXECUTIONS; i++)); do
        output_file="output/execution_${i}.csv"

        if [ -e "$output_file" ]; then
          value=$(grep "^${iteration};" "$output_file" | cut -d ';' -f 2)

          if [ -n "$value" ]; then
            sum=$(awk "BEGIN {printf \"%f\", $sum + $value}")
            count=$((count + 1))
          fi
        fi
      done

      if [ "$count" -gt 0 ]; then
          mean=$(awk "BEGIN {printf \"%f\", $sum / $count}")
          echo "${iteration};${mean}" >> "$mean_file"
      fi
    done
    cd ..
  done
  cd ..
done
