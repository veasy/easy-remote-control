#!/usr/bin/env bash
if [ "$(uname)" == "Darwin" ]; then
    echo "install autopy on MacOSX..."
    # specialized install of autopy
    brew install libpng
    CFLAGS="-Wno-return-type" pip install git+https://github.com/potpath/autopy.git
fi

pip install -r requirements.txt