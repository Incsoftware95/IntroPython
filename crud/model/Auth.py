
from model.Security import Security
import bcrypt

class Auth(Security):
    
    def __init__(self,email:str,passwd:str) -> None:
        super().__init__()
        self.__email = email
        self.__passwd =   passwd
        self.__saltV =  bcrypt.gensalt(12)
        self.__hash = ""
       

    def get_email(self)->str:
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_passwd(self):
        return self.__passwd

    def set_passwd(self, passwd):
        self.__passwd = self.encrypt(passwd)

    def __str__(self) -> str:
        super().__str__()

        return f"Email: {self.get_email()}"
    
    def encrypt(self):
        super().encrypt()
        passwdByte =self.__passwd.encode('utf-8')
        passwdHash =bcrypt.hashpw(password=passwdByte,salt=self.__saltV)
        self.__hash = passwdHash
        self.__passwd = passwdHash.hex()
        
    
    def dcrypt(self, passwd:str):
        super().dcrypt(passwd)

        if bcrypt.hashpw(passwd.encode("utf-8"),self.__hash)== self.__hash:
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False

    

