import os, sys
import argparse
import configparser
import logging

class CLI:
    CLI_VERSION = "CLI 1.0.0"
    INI_FILE = "cli_init.ini"

    def __load_ini_file(self, filename):
        full_path = os.path.abspath(os.path.join("./src", filename))
        path_config_file = full_path if os.path.isfile(full_path) else \
            os.path.abspath(os.path.join(os.path.dirname(sys.executable), filename))
        self.config = configparser.ConfigParser()
        if self.config.read(path_config_file):
            return True
        else:
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='cli.log')
            logging.error("Não foi possível carregar o arquivo de configuração em {}".format(path_config_file))
            return False

    def __init__(self):
        if self.__load_ini_file(self.INI_FILE):
            self.__run()

    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog="project",
            description="Automação para criar projetos",
            epilog="Develop by: Roberto Chaves",
            usage="%(prog)s [options]")

        self.parser.version = self.CLI_VERSION
        self.parser.add_argument("-c","--create", help="Criar Projeto")
        self.parser.add_argument("-v","--view", help="Criar uma nova view")
        parser_args = self.parser.parse_args()
        
        if parser_args:
            try:
                if parser_args.create:
                    self.__create_project(parser_args.create)
                elif parser_args.view:
                    self.__create_view(parser_args.view)
            except Exception as e:
                print("Argumento inválido: {}".format(e))
                sys.exit(1)
        else:
            self.parser.print_help()
            sys.exit(1)
  
    def __create_project(self,args):
       print(args)
       print("chamou o create")
    
    def __create_view(self,args):
       print(args)
       print("chamou o view")
    
    
