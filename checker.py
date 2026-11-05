from db import get_data


def version_key(version):
    parts = version.split('.')
    numbers = []

    for part in parts:
        if not part.isdigit():
            raise ValueError("Версия должна состоять из чисел через точку")
        numbers.append(int(part))
    while len(numbers) > 1 and numbers[-1] == 0:
        numbers.pop()
    return numbers


def is_vulnerabilities(version, start, fixed):
    version_parts = version_key(version)
    start_parts = version_key(start)
    fixed_parts = version_key(fixed)

    return start_parts <= version_parts <= fixed_parts


def find_safe_version(product):
    versions, vuln = get_data(product)
    safe_version = None

    for row in versions:
        version = row[0]
        found = False

        for v in vuln:
            if is_vulnerabilities(version, v[3], v[4]):
                found = True
                break

        if found:
            continue

        if safe_version is None:
            safe_version = version
        elif version_key(version) > version_key(safe_version):
            safe_version = version

    return safe_version


def find_vulnerabilities(product, version):
    version_key(version)
    vuln = get_data(product)[1]
    result = []

    for v in vuln:
        if is_vulnerabilities(version, v[3], v[4]):
            result.append(v)

    return result
