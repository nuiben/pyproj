#!/usr/bin/env python3

import datetime, emails, reports, os

def write_paragraph(path):
    records = []
    for filename in os.listdir(path):
        with open(path + filename, "r") as f:
            lines = f.read().splitlines()[:2]
            record = dict(zip(("name", "weight"), lines))
            for key, value in record.items():
                records.append(key+": "+value+"<br/>")
            records.append("<br/>")
    return "".join(records)


if __name__ == "__main__":
    now = datetime.datetime.now()
    title = "Processed Update on ["+now.strftime('%D')+"]"
    path = "./supplier-data/descriptions/"
    paragraph = write_paragraph(path)
    reports.generate_report("/tmp/processed.pdf", title, paragraph)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
