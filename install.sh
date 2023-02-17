#!/bin/bash

RED="\e[31m"
YELLOW="\e[33m"
GREEN="\e[32m"
END="\e[0m"
BOLD="\e[1m"

check_if_done() {
  if [ $? -eq 0 ]; then
    echo -e "${GREEN}$1${END}"
  else
    echo -e "${RED}Aborted${END}"
    exit 1
  fi  
}

press_any_key_to_continue() {
  echo "Press any key to continue..."
  read -r -n 1 -s answer
}

clone_repository() {
  if [[ -d UserApplication ]]; then
    rm -fr UserApplication
  fi
  local repo_link="git@github.com:shreyas-acharya/UserApplication.git"
  git clone $repo_link
  check_if_done "Cloning successful"
}

create_env_file() {
  cd UserApplication
  if [[ -e .env ]]; then
    rm .env
  fi
  touch .env  
  echo -n "Enter a username (Default: root) : "
  read username
  echo "USERNAME=${username:-root}" >> .env
  echo -n "Enter a password (Default: root) : "
  read password
  echo "PASSWORD=${password:-root}" >> .env
  echo -n "Enter database name (Default: user) : "
  read database
  echo "DATABASE=${database:-user}" >> .env
  check_if_done "Created .env file"
}

run_container() {
  sudo docker compose up
  sudo docker compose down
  check_if_done "Containers removed..."
}

main() {
  echo -e "${BOLD}User Management Application${END}test"
  echo
  echo -e "${BOLD}Step 1: ${END}Clone git repository"
  clone_repository
  echo
  echo -e "${BOLD}Step 2: ${END}Create .env file"
  create_env_file
  echo
  echo -e "${BOLD}Step 3: ${END}Create and run container"
  run_container  
}

main

