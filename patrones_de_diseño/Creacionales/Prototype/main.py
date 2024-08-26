from concrete_prototype import SystemConfigPrototype

def main():
    # Diccionario con la configuración
    # del sistema
    config = {
        "OS" : "Linux",
        "Version" : "Ubuntu 18.04"
    }

    # Instancia de 'SystemConfigPrototype'
    original_config = SystemConfigPrototype(config)
    # Clonamos e imprimimos
    cloned_config = original_config.clone()
    print("Configuración original: {}".format(original_config.configuration))
    print("Configuración clonada: {}".format(cloned_config.configuration))

if __name__ == "__main__":
    main()