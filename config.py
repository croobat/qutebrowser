# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

import subprocess
import os
from qutebrowser.api import interceptor

# Load existing settings made via :set
config.load_autoconfig()

# Pages
c.url.default_page = 'https://www.google.com'
c.url.start_pages = 'https://www.google.com'
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}',
                       'yt': 'https://www.youtube.com/results?search_query={}',
                       'am': 'https://www.amazon.com/s?k={}',
                       'ml': 'https://listado.mercadolibre.com.mx/{}',
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'aur': 'https://archlinux.org/packages/?sort=&q={}',
                       'pex': 'https://www.pexels.com/search/{}',
                       'gh': 'https://github.com/search?q={}',
                       'pirate': 'https://thepiratebay.org/search.php?q={}',
                       'red': 'https://www.reddit.com/r/{}',
                       'wiki': 'https://en.wikipedia.org/wiki/{}'}

c.completion.web_history.exclude = [
    'google.com'
]

# Aliases
c.aliases = {'q': 'close',
             'qa': 'quit',
             'w': 'session-save',
             'wq': 'quit --save',
             'wqa': 'quit --save',
             }

# Bindings
bindings = {
    # Faster
    '<Ctrl-j>': 'run-with-count 15 scroll down',
    '<Ctrl-k>': 'run-with-count 15 scroll up',
    # VIM like
    't': 'set-cmd-text -s : open -t',
    'xb': 'config-cycle statusbar.show always never',
    'xt': 'config-cycle tabs.show always never',
     'xx': 'config-cycle statusbar.show always never;; config-cycle tabs.show always never',
    'j': 'run-with-count 3 scroll down',
    'k': 'run-with-count 3 scroll up',
    'J': 'tab-prev',
    'K': 'tab-next',
    'ZQ': 'quit',
    'ZZ': 'quit --save',
    # Hints
    'yf': 'hint links yank',
    'yF': 'hint all yank',
    # Stylesheets
    ',,': 'greasemonkey-reload ;; reload',
    ',z': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/apprentice/apprentice-all-sites.css ""',
    ',x': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/darculized/darculized-all-sites.css ""',
    ',c': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css ""',
    ',v': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-dark/solarized-dark-all-sites.css ""',
    ',b': 'config-cycle content.user_stylesheets ~/.config/qutebrowser/solarized-everything-css/css/solarized-light/solarized-light-all-sites.css ""'
}
for binding in bindings:
    config.bind(binding, bindings[binding])

insertBindings = {
    "<Ctrl-h>": "fake-key <Backspace>",
    "<Ctrl-a>": "fake-key <Home>",
    "<Ctrl-e>": "fake-key <End>",
    "<Ctrl-b>": "fake-key <Left>",
    "<Mod1-b>": "fake-key <Ctrl-Left>",
    "<Ctrl-f>": "fake-key <Right>",
    "<Mod1-f>": "fake-key <Ctrl-Right>",
    "<Ctrl-p>": "fake-key <Up>",
    "<Ctrl-n>": "fake-key <Down>",
    "<Mod1-d>": "fake-key <Ctrl-Delete>",
    "<Ctrl-d>": "fake-key <Delete>",
    "<Ctrl-w>": "fake-key <Ctrl-Backspace>",
    "<Ctrl-u>": "fake-key <Shift-Home><Delete>",
    "<Ctrl-k>": "fake-key <Shift-End><Delete>"
}
for binding in insertBindings:
    config.bind(binding, insertBindings[binding], 'insert')

# Fonts
c.fonts.default_family = 'JetBrainsMono Nerd Font'
c.fonts.default_size = '10.5pt'

# Smooth scrolling
c.scrolling.smooth = True

# Youtube autoplay
c.content.autoplay = False

# Value to use for `prefers-color-scheme:` for websites. The "light"
# value is only available with QtWebEngine 5.15.2+. On older versions,
# it is the same as "auto". The "auto" value is broken on QtWebEngine
# 5.15.2 due to a Qt bug. There, it will fall back to "light"
# unconditionally.
# Type: String
# Valid values:
#   - auto: Use the system-wide color scheme setting.
#   - light: Force a light theme.
#   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = 'dark'
config.set("colors.webpage.darkmode.enabled", True)

# Downloads location
c.downloads.location.directory = '~/Downloads'
c.downloads.prevent_mixed_content = False

# Disable certificate
c.content.tls.certificate_errors = 'load-insecurely'

# --------------------------------------------------------------

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Time interval (in milliseconds) between auto-saves of
# config/cookies/etc.
# Type: Int
c.auto_save.interval = 15000

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language',
           '', 'https://matchmaker.krunker.io/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent',
           'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent',
           'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
config.set('content.headers.user_agent',
           'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
config.set('content.notifications.enabled', True, 'https://www.reddit.com')

# Editor (and arguments) to use for the `edit-*` commands. The following
# placeholders are defined:  * `{file}`: Filename of the file to be
# edited. * `{line}`: Line in which the caret is found in the text. *
# `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['vim', '-f', '{file}', '-c', 'normal {line}G{column0}l']

# When to show the statusbar.
# Type: String
# Valid values:
#   - always: Always show the statusbar.
#   - never: Always hide the statusbar.
#   - in-mode: Show the statusbar when in modes other than normal mode.
c.statusbar.show = 'never'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Color scheme
import dracula.draw
dracula.draw.blood(c)

# Load custom stylesheet
c.content.user_stylesheets =  ['~/.config/qutebrowser/styles.css']
