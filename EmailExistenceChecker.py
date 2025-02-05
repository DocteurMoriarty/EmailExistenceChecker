import dns.resolver
import smtplib
import sys

if dns.__version__ == "2.7.0":
    print("[...] VERSION ",dns.__version__,"[OK]")
else:
    print("[...] VERSION ",dns.__version__,"[KO]")
    print("[\o/] pip install dnspython==2.7.0")
    sys.exit(1)


def get_mx_records(domain):
    print("GET MX RECORD...")
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [str(mx.exchange) for mx in mx_records]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return []
def check_email_exists(email):
    domain = email.split('@')[1]
    mx_records = get_mx_records(domain)
    if not mx_records:
        print(f"[!!!] {domain} [MX NOT FOUND].")
        return False
    for mx in mx_records:
        try:
            with smtplib.SMTP(mx) as server:
                server.set_debuglevel(False)
                server.ehlo()
                server.mail('')
                code, message = server.rcpt(email)
                if code == 250:
                    print(f"[VVV] {email} [EXISTS]")
                    return True
                else:
                    print(f"[XXX] {email} [NOT EXISTS]")
                    return False
        except Exception as e:
            print(f"[!!!] ERROR {email}: {e}")
            continue
    print(f"[!!!] REQUEST NOT POSSIBLE {email}.")
    return False
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python emailActiv.py <email>")
        sys.exit(1)

    email_to_check = sys.argv[1]
    check_email_exists(email_to_check)
