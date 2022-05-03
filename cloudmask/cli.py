import fire
from cloudmask import __version__

class CloudMaskCLI:
    @staticmethod
    def version():
        return __version__

def main():
    fire.Fire(CloudMaskCLI)

if __name__=='__main__':
    main()