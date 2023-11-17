#!/bin/bash

# List of parameters
hypotheses=(peter common)
strategies=(best worst random)

# Loop para iterar sobre os valores das variáveis
for hypothesis in "${hypotheses[@]}"; do
  mkdir $hypothesis
  cd $hypothesis

  for strategy in "${strategies[@]}"; do
    mkdir $strategy
    cd $strategy

    mkdir output

    cd ..
  done
  cd ..
done
