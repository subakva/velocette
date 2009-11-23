#!/bin/bash
if [ ! -n "$1" ]; then
  echo "Usage: init_project.sh environment_name"
else
  export PYTHONPATH=.:$PWD/lib
  ENV_NAME=$1

  echo "--------------------------------------------------"
  echo "Installing required libraries..."
  echo "--------------------------------------------------"
  ./bin/install_libs.sh

  echo "--------------------------------------------------"
  echo "Refreshing the environment..."
  echo "--------------------------------------------------"
  ./bin/setup_env.sh $ENV_NAME

  echo "--------------------------------------------------"
  echo "Resetting the database..."
  echo "--------------------------------------------------"
  ./manage.py reset_db

  echo "--------------------------------------------------"
  echo "Running dmigrate..."
  echo "--------------------------------------------------"
  ./manage.py dmigrate all

  echo "--------------------------------------------------"
  echo "Loading initial data..."
  echo "--------------------------------------------------"
  ./manage.py loaddata fixtures/initial_data.json

  echo "--------------------------------------------------"
  echo "Deleting errant pyc files..."
  echo "--------------------------------------------------"
  ./bin/purge.py .
fi
