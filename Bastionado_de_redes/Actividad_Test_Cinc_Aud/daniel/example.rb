title "Verificación básica de aplicación .NET en Docker"

control "dotnet-process-1.0" do
  impact 0.7
  title "El proceso de .NET está en ejecución"
  desc "Comprueba que el proceso dotnet esté activo dentro del contenedor"

  # Verifica que el proceso principal de .NET esté corriendo
  describe processes('dotnet') do
    it { should exist }
  end
end

control "app-folder-1.0" do
  impact 0.5
  title "Directorio de la aplicación existe"
  desc "Verifica que el código o la carpeta de la app esté presente"

  # Cambia la ruta según dónde montes tu app dentro del contenedor
  describe file('/app') do
    it { should exist }
    it { should be_directory }
  end
end