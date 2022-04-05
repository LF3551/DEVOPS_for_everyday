class IPAddress:
    def __init__(self, address, mask):
        self._address = address
        self._mask = int(mask)
# makes all vaiables only for reading
    @property
    def mask(self):
        return self._mask
    @property
    def ip(self):
        return self._address

if __name__ == '__main__':
    ip1 = IPAddress('10.1.1.1', 24)
    print(ip1.mask)
    print(ip1.ip)
