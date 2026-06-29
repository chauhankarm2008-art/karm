import hashlib

def generate_hash(text, algorithm):

    text = text.encode()

    if algorithm == "MD5":
        return hashlib.md5(text).hexdigest()

    elif algorithm == "SHA1":
        return hashlib.sha1(text).hexdigest()

    elif algorithm == "SHA256":
        return hashlib.sha256(text).hexdigest()

    elif algorithm == "SHA512":
        return hashlib.sha512(text).hexdigest()

    return "Invalid Algorithm"