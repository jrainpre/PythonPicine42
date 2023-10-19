# Allowed functions : time, datetime or any other library that allows to
# receive the date


# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>

import datetime

current_date = datetime.datetime.now()
old = datetime.datetime(1970,1,1)
new = current_date.timestamp() - old.timestamp()
seconds = "{:,.4f}".format(new)
sci_not = "{:.2e}".format(new)

text = ["Seconds since January 1, 1970:"]
text.append(seconds)
text.append("or")
text.append(sci_not)
text.append("in scientific notation")
print(*text)
print(current_date.strftime("%b %d %Y"))



