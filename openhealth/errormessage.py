from rest_framework.exceptions import ErrorDetail


def Errormessage(e):
    z = (ErrorDetail(e).split("[")[-1].split(",")[0].split("=")[-1])
    return z.strip("'")
