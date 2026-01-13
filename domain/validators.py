class CafeaException(Exception):
    pass
class Validator:
    def validate(self,cafea):
        if cafea.pret<=0:
            raise CafeaException("Pretul cafelei e negativ")