# copyright: 2018, The Authors

title "Tests para servicios nginx"

control "nginx-service-1.0" do
  impact 1.0
  title "Comprobar que nginx esta activo y corriendo"
  desc "Verifica que el servicio nginx esta instalado y en ejecucion, muestra la version y comprueba el puerto 8081."

  describe service('nginx') do
    it { should be_installed }
    it { should be_running }
  end

  describe command('nginx -v') do
    its('stderr') { should match /nginx\/\d+\.\d+\.\d+/ }
end 

  describe port(8081) do
    it { should be_listening }
  end
end
