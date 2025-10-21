# copyright: 2018, The Authors

title "nginx test tests"

# controls/nginx_spec.rb
control 'nginx-01' do
  impact 1.0
  title 'NGINX debe estar instalado'
  desc 'Verficar que el paquete nginx este instalado'
  describe package('nginx') do
    it { should be_installed }
  end
end

control 'nginx-02' do
  impact 1.0
  title 'servicio nginx instalado, activo y habilitado'
  desc 'El servicio nginx debe estar corriendo y habilitado'
  describe service('nginx') do
    it { should be_installed }
    it { should be_enabled }
    it { should be_running }
  end
end

control 'nginx-03' do
  impact 0.9
  title 'Puerto 80 escuchando'
  describe port(80) do
    it { should be_listening }
    its('protocols') { should include 'tcp' }
  end
end

control 'nginx-04' do
  impact 0.7
  title 'nginx.conf debe tener server_tokens off'
  desc 'Para ocultar la versión del servidor'
  describe nginx_conf do
    its('server_tokens') { should cmp 'off' }
  end
end

control 'nginx-05' do
  impact 0.8
  title 'Archivo index.html contiene texto esperado'
  desc 'Comprobar que la pagina de prueba contiene "Welcome"'
  describe file('/usr/share/nginx/html/index.html') do
    it { should exist }
    its('content') { should match /Welcome/i }
  end
end

