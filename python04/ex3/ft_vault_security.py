#! /usr/bin/env python3


def secure_archive(
        file: str,
        action: str = "",
        content: str = ""
        ) -> tuple[bool, str]:
    if action == "w":
        with open(file, action) as f:
            f.write(content)
            return (True, "Content successfully written to file")
    else:
        try:
            with open(file) as f:
                content = f.read()
        except OSError as e:
            return (False, str(e))
        return (True, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from a inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "w", result[1]))
