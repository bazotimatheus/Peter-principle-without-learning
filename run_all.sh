#!/bin/bash

# Defina o caminho do arquivo .py
parameters_py="config.py"
exec_py="main.py"

# Parameters
hypotheses=(peter common)
strategies=(best worst random)

# Loop para iterar sobre os valores das variáveis
for hypothesis in "${hypotheses[@]}"; do
  for strategy in "${strategies[@]}"; do
    cd peter

    sed -i "s/HYPOTHESIS = .*/HYPOTHESIS = '$hypothesis'/" $parameters_py
    sed -i "s/STRATEGY = .*/STRATEGY = '$strategy'/" $parameters_py

    cd ..

    python3 $exec_py
  done
done
