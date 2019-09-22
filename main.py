from multiping import MultiPing
from lib.sendgrid import sendMail


def main():
    addrs = ["192.168.0.1", "192.168.0.2", "192.168.0.3", "192.168.0.25"]
    print("sending one round of pings and checking twice for responses")
    mp = MultiPing(addrs)
    mp.send()

    responses, no_responses = mp.receive(1)

    print("   received responses:  %s" % list(responses.keys()))
    print("   no responses so far: %s" % no_responses)

    print("sending again, but waiting with retries if no response received")

    mp = MultiPing(addrs)
    for i in range(3):
        mp.send()
        responses, no_response = mp.receive(1)

        print("    received responses:     %s" % list(responses.keys()))
        if not no_response:
            print("    all done, received responses from everyone")
            break
        else:
            print("    %d. retry, resending to: %s" % (i + 1, no_response))
    if no_response:
        print(
            "    no response received in time, even after 3 retries: %s" % no_response
        )
        sendMail(no_response)
    print("")


if __name__ == "__main__":
    main()
