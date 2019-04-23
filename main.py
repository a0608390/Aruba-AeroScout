from message import *
from socketserver import *
import time

aps = {}


class ArubaAero(BaseRequestHandler):
    def handle(self):
        print(aps)
        try:
            while True:
                pkt = self.request[0]
                server = self.request[1]
                addr = self.client_address
                ap_msg = Msg(pkt)
                ap_msg.view()

                # update aps dict
                if aps.get(ap_msg.data_payload.get('ap_mac_address')) is None:
                    aps[ap_msg.data_payload.get('ap_mac_address')] = [addr, ap_msg.code, 0]
                elif aps[ap_msg.data_payload.get('ap_mac_address')][0] != addr:
                    aps[ap_msg.data_payload.get('ap_mac_address')] = [addr, ap_msg.code, 0]
                else:
                    pass

                # confirm send ae message
                if ap_msg.code == b'\xD9' and aps[ap_msg.data_payload.get('ap_mac_address')][1] == b'\xD9':
                    aps[ap_msg.data_payload.get('ap_mac_address')][2] += 1
                    set_msg = ap_msg.B0_pkt(aps[ap_msg.data_payload.get('ap_mac_address')][2])
                    server.sendto(set_msg, addr)
                    break

                elif ap_msg.code == b'\xD2' and aps[ap_msg.data_payload.get('ap_mac_address')][1] == b'\xD9':
                    aps[ap_msg.data_payload.get('ap_mac_address')][2] += 1
                    aps[ap_msg.data_payload.get('ap_mac_address')][1] = ap_msg.code
                    set_msg = ap_msg.B1_pkt(aps[ap_msg.data_payload.get('ap_mac_address')][2])
                    server.sendto(set_msg, addr)
                    break

                elif ap_msg.code == b'\xD4' and aps[ap_msg.data_payload.get('ap_mac_address')][1] == b'\xD2':
                    aps[ap_msg.data_payload.get('ap_mac_address')][2] += 1
                    aps[ap_msg.data_payload.get('ap_mac_address')][1] = ap_msg.code
                    set_msg = ap_msg.B2_pkt(aps[ap_msg.data_payload.get('ap_mac_address')][2])
                    server.sendto(set_msg, addr)
                    break

                elif ap_msg.code == b'\xD0' and aps[ap_msg.data_payload.get('ap_mac_address')][1] == b'\xD4':
                    aps[ap_msg.data_payload.get('ap_mac_address')][2] += 1
                    aps[ap_msg.data_payload.get('ap_mac_address')][1] = ap_msg.code
                    set_msg = ap_msg.B4_pkt(aps[ap_msg.data_payload.get('ap_mac_address')][2])
                    server.sendto(set_msg, addr)
                    break
                else:
                    aps[ap_msg.data_payload.get('ap_mac_address')][1] = ap_msg.code
                    break
        except Exception as msg:
            print(msg)


if __name__ == '__main__':
    host = ('10.10.254.27', 12092)

    server = UDPServer(host, ArubaAero)
    server.serve_forever()
