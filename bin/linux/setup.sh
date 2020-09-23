
LINK=$(readlink -f "0")
BASEDIR=$(dirname "$LINK")
ICON="${BASEDIR}/Icon.png"
EXE="${BASEDIR}/CurrencyCalculator"
chmod +x CurrencyCalculator
echo "[Desktop Entry]
Name=CurrencyCalculator
Exec="\"${EXE}\""
Icon="${ICON}"
Terminal=false
Type=Application
" >> /usr/share/applications/CurrencyCalculator.desktop