"""
Example using the netrc to storage credentials

Set a path for your netrc file or ~/.netrc to default path
Get login, account and password of netrc file
"""
import netrc


if __name__ == "__main__":
    GET = netrc.netrc('netrc-file')

    print(GET.authenticators('my-host'))
