# PART 1. HYPERVISORS #
 ## What are the most popular hypervisors for infrastructure virtualization? ##
 >Hyper-V, KVM, vSphere , XenServer,VMware
## Briefly describe the main differences of the most popular hypervisors. ##
 >The main difference between hypervisors:
 Some hypervisors work immediately on hardware without an OS, while others create virtual machines under the main OS as HyperV.
 Difference in GUIs and usage and license costs.

#PART 2. WORK WITH VIRTUALBOX

# 1)Install ISO
![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/DeepinScreenshot_VirtualBox_20201212170032.png)

# 2)Gruops VM
 ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/DeepinScreenshot_select-area_20201212160153.png)
 
# 3)USB and folder share
  ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/DeepinScreenshot_VirtualBox_20201212172526.png)
  ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/usbshare.png)
  ![Image ]( https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/shareforder.png)
  
# 4)NetworkVB
 ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/HostNetworkmanager.png)
 ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/%D1%81onnecr%20Bridje.png)
 ![Image ](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/HostNetworkmanagerPrufIp.png)
 
# 5)VB console
![Image](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/runterminalVB.png)

# 6)Vagrant

![Image](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/VagrantconnectSSH.png)
## my littel box
![Image](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/Vagrantup.png)
![Image](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module2/task2.1/screenimage/MyvagrantBox.png)

# 7)My Vagrantfile(install sql and apache)
```ruby
  
  Vagrant.configure(2) do |config|

  config.vm.box = "bento/ubuntu-18.04"
  config.vm.box_check_update = false
  config.ssh.insert_key = false

  
  config.vm.define "web-server" do |subconfig|
  
    subconfig.vm.provider "virtualbox" do |vb|
      vb.name = "apache-server"
    end
    # hostname виртуальной машины
    subconfig.vm.hostname = "apache-server"
    # настройки сети
    subconfig.vm.network "private_network", ip: "192.168.53.3"
    # установка пакетов
    subconfig.vm.provision "apache", type: "shell", inline: "apt-get install -y apache2"
  end

  
  config.vm.define "sql-server" do |subconfig|
    # имя виртуальной машины
    subconfig.vm.provider "virtualbox" do |vb|
      vb.name = "mysql-server"
    end
    # hostname виртуальной машины
    subconfig.vm.hostname = "mysql-server"
    # настройки сети
    subconfig.vm.network "private_network", ip: "192.168.53.4"
    
    subconfig.vm.provision "mysql", type: "shell", inline: "apt-get install -y mysql-server"
  end
  
  # обновление системы (для первой и второй)
  config.vm.provision "update", type: "shell", inline: "apt-get update && apt-get upgrade -y"
end
```ruby
  
