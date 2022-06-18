def remove_comments(s: str) -> str:
    stack = []
    i = 0
    print(list(s))
    while i < len(s):
        c = s[i]
        if c == "*" and stack and stack[-1] == "/":
            idx = i + 2
            while idx < len(s) and s[idx - 1] != "*" and s[idx] != "/":
                idx += 1
            stack.pop()
            i = idx
        elif stack and c == "/" and stack[-1] == "/":
            idx = i + 1
            while idx < len(s) and s[idx] != "\n":
                idx += 1
            stack.pop()
            i = idx
        elif c == '"':
            stack.append(c)
            idx = i + 1
            while idx < len(s) and s[idx] != '"':
                stack.append(s[idx])
                idx += 1
            if idx < len(s):
                stack.append(s[idx])
            i = idx
        else:
            stack.append(c)
        i += 1
    print(stack)
    return "".join(stack)


# после однострочный комментариев появляется
print(
    remove_comments(
        """
        int someMethod() {
            a = 5
            // comment
            return a + 1;
        }
        """
    )
)

# print(
#     remove_comments(
#         """
#         int someMethod() {
#             int a = 5;

#             String myStr = " //* comment at the end of line*/ /* comment still continues */";
#             return a + 1;
#         }
#         """
#     )
# )

# print(
#     remove_comments(
#         """
#         /*
#         several strings
#         */
#         int someMethod() {
#             int a = 5;
#             // какой-то однострочный коммент
#             // f
#             String myStr = " //* comment at the end of line*/ /* comment still continues */";
#             return /* changed code */ a + 1;
#         }
#         """
#     )
# )
