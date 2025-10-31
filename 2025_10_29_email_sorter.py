def sort(emails):
    emails_array= []
    for e in emails:
        emails_array.append(e.split("@"))

    result = []
    sorted_emails_list = sorted(emails_array, key=lambda s: (s[1].lower(), s[0].lower()))
    for s in sorted_emails_list:
        result.append("@".join(s))
    return result

test = sort(["jill@mail.com", "john@example.com", "jane@example.com"])
print(test)