# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "kivybox"
  config.vm.network "private_network", ip: "10.0.0.99"
  config.vm.synced_folder ".", "/srv", owner: "vagrant", group: "vagrant"

  forward_port = ->(guest, host = guest) do
    config.vm.network :forwarded_port,
      guest: guest,
      host: host,
      auto_correct: true
  end

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    # vb.gui = true
  end

  config.vm.provision :shell, :path => "provision.sh"
end
