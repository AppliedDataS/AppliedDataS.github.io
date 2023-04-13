#!/bin/zsh
echo "This program takes a string i.e your github email address"
echo "and copies the generated SSH key to the clipboard"
printf "%s" "Enter your email address: "
read EMAIL
ssh-keygen -t ed25519 -C "$EMAIL"
eval "$(ssh-agent -s)"
echo "Host github.com" > ~/.ssh/config
echo "AddKeysToAgent yes" >> ~/.ssh/config
echo "UseKeychain yes" >> ~/.ssh/config
echo "IdentityFile ~/.ssh/id_ed25519" >> ~/.ssh/config
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
pbcopy < ~/.ssh/id_ed25519.pub
