#!/bin/bash
if [ ! -n "$1" ]; then
  echo "Usage: setup_env.sh environment_name"
else
  export PYTHONPATH=.:$PWD/lib
  ENV_NAME=$1

  echo "--------------------------------------------------"
  echo "Setting up environment-specific settings..."
  echo "--------------------------------------------------"
  cp -i env/$ENV_NAME.settings.py env/_local.py

  echo "--------------------------------------------------"
  echo "Updating link to admin media..."
  echo "--------------------------------------------------"
  rm -i static/admin
  ln -s $PWD/lib/django/contrib/admin/media/ static/admin

  # echo "--------------------------------------------------"
  # echo "Installing crontab..."
  # echo "--------------------------------------------------"
  # echo "Q. Install new crontab (old crontab will be over-written) (y/n)?"
  # read confirm
  # if [ "$confirm" = "y" ]; then
  #   crontab env/$ENV_NAME.crontab.txt
  # fi
fi
