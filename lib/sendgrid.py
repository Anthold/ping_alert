from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendMail(host_down):
    """
    Send the mail using sendgrid in this case
    """
    host_str = ",\n".join(host_down)
    message = Mail(
        from_email="MAIL SENDER",
        to_emails="MAIL DESTINATION",
        subject="ping_alert = host down",
        html_content="<strong>ping_alert</strong> : \n no answer from hosts : \n\n"
        + host_str,
    )
    try:
        sg = SendGridAPIClient("CLE SENDGRID A REMPLACER")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
