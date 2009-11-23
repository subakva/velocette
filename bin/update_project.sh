#!/bin/bash
if [ ! -n "$1" ]; then
  echo "Usage: update_project.sh environment_name"
else
  export PYTHONPATH=.:$PWD/lib
  ENV_NAME=$1

  echo "--------------------------------------------------"
  echo "Refreshing the environment..."
  echo "--------------------------------------------------"
  ./bin/setup_env.sh $ENV_NAME

  echo "--------------------------------------------------"
  echo "Running dmigrate..."
  echo "--------------------------------------------------"
  ./manage.py dmigrate all

  echo "--------------------------------------------------"
  echo "Deleting errant pyc files..."
  echo "--------------------------------------------------"
  ./bin/purge.py .
fi
