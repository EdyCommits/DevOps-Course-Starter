
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
	sudo apt-get update
	
	# Install pyenv prerequisites
	sudo apt-get install -y build-essential libssl1.0-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
	
	# Set the profile and the env if this is not done before
	if [ !$PYENV_ROOT ]
	then
		# Install pyenv
		git clone https://github.com/pyenv/pyenv.git ~/.pyenv
		echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
		echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
		echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
	fi
	
	# Install python 3.9.1
	pyenv install 3.9.1
	pyenv global 3.9.1
	
	# Install poetry
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
	source ~/.profile
	
	
  SHELL
  config.vm.network "forwarded_port", guest: 5000, host: 1111
  config.trigger.after :up do |trigger|
	trigger.name = "Launching TODO app"
	trigger.info = "Running the app setup script"
	trigger.run_remote = { privileged: false, inline: "
		# Install dependencies and launch
		cd /vagrant
		poetry install
		nohup poetry run flask run --host 0.0.0.0 > logs.txt 2>&1 &
				
	"}
	end
end