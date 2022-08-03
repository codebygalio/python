window = this;
function Base64() {
  // private property
  _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  // public method for encoding
  this.encode = function (input) {
      var output = "";
      var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
      var i = 0;
      input = _utf8_encode(input);
      while (i < input.length) {
          chr1 = input.charCodeAt(i++);
          chr2 = input.charCodeAt(i++);
          chr3 = input.charCodeAt(i++);
          enc1 = chr1 >> 2;
          enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
          enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
          enc4 = chr3 & 63;
          if (isNaN(chr2)) {
              enc3 = enc4 = 64;
          } else if (isNaN(chr3)) {
              enc4 = 64;
          }
          output = output +
              _keyStr.charAt(enc1) + _keyStr.charAt(enc2) +
              _keyStr.charAt(enc3) + _keyStr.charAt(enc4);
      }
      return output;
  }

  // public method for decoding
  this.decode = function (input) {
      var output = "";
      var chr1, chr2, chr3;
      var enc1, enc2, enc3, enc4;
      var i = 0;
      input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
      while (i < input.length) {
          enc1 = _keyStr.indexOf(input.charAt(i++));
          enc2 = _keyStr.indexOf(input.charAt(i++));
          enc3 = _keyStr.indexOf(input.charAt(i++));
          enc4 = _keyStr.indexOf(input.charAt(i++));
          chr1 = (enc1 << 2) | (enc2 >> 4);
          chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
          chr3 = ((enc3 & 3) << 6) | enc4;
          output = output + String.fromCharCode(chr1);
          if (enc3 != 64) {
              output = output + String.fromCharCode(chr2);
          }
          if (enc4 != 64) {
              output = output + String.fromCharCode(chr3);
          }
      }
      //output = _utf8_decode(output);
      return output;
  };

  // private method for UTF-8 encoding
  _utf8_encode = function (string) {
      string = string.replace(/\r\n/g,"\n");
      var utftext = "";
      for (var n = 0; n < string.length; n++) {
          var c = string.charCodeAt(n);
          if (c < 128) {
              utftext += String.fromCharCode(c);
          } else if((c > 127) && (c < 2048)) {
              utftext += String.fromCharCode((c >> 6) | 192);
              utftext += String.fromCharCode((c & 63) | 128);
          } else {
              utftext += String.fromCharCode((c >> 12) | 224);
              utftext += String.fromCharCode(((c >> 6) & 63) | 128);
              utftext += String.fromCharCode((c & 63) | 128);
          }

      }
      return utftext;
  };

  // private method for UTF-8 decoding
  _utf8_decode = function (utftext) {
      var string = "";
      var i = 0;
      var c = c1 = c2 = 0;
      while ( i < utftext.length ) {
          c = utftext.charCodeAt(i);
          if (c < 128) {
              string += String.fromCharCode(c);
              i++;
          } else if((c > 191) && (c < 224)) {
              c2 = utftext.charCodeAt(i+1);
              string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
              i += 2;
          } else {
              c2 = utftext.charCodeAt(i+1);
              c3 = utftext.charCodeAt(i+2);
              string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
              i += 3;
          }
      }
      return string;
  };
}
var base64 = new Base64();
document = {}
window.atob = base64.decode;
window.eval = eval;
window.String = String;
window.parseInt = parseInt;

var _0x3012 = ['\x73\x75\x62\x73\x74\x72\x69\x6e\x67', '\x61\x74\x6f\x62', '\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74', '\x70\x75\x73\x68', '\x74\x65\x73\x74'];
(function (_0x3ed35c, _0x48b8fe) {
    var _0x1ad9d9 = function (_0x8eeda7) {
        while (--_0x8eeda7) {
            _0x3ed35c['push'](_0x3ed35c['shift']());
        }
    };
    _0x1ad9d9(++_0x48b8fe);
}(_0x3012, 0x153));
var _0x3a8e = function (_0xc40c11, _0x32bbb2) {
    _0xc40c11 = _0xc40c11 - 0x0;
    var _0x4e269a = _0x3012[_0xc40c11];
    return _0x4e269a;
};
!function (_0xcbc80b) {
    _0xcbc80b['\x64\x65\x63\x6f\x64\x65\x5f\x64\x65\x73\x63'] = function g(_0x1c0cdf) {
        if (_0x1c0cdf = _0x1c0cdf['\x72\x65\x70\x6c\x61\x63\x65'](/^\s+|\s+$/g, ''),
            !/^@[\s\S]*@$/[_0x3a8e('0x0')](_0x1c0cdf))
            return _0x1c0cdf;
        var _0x36ab38 = (/\b_k=([^;]*)/['\x65\x78\x65\x63'](document['\x63\x6f\x6f\x6b\x69\x65']) || [])[0x1] || '';
        if (_0x1c0cdf = _0x1c0cdf['\x72\x65\x70\x6c\x61\x63\x65'](/^@|@$/g, ''),
            /^[^@]+@[\s\S]+/['\x74\x65\x73\x74'](_0x1c0cdf)) {
            var _0x33c80e = _0x1c0cdf['\x69\x6e\x64\x65\x78\x4f\x66']('\x40');
            _0x36ab38 = _0x1c0cdf[_0x3a8e('0x1')](0x0, _0x33c80e),
                _0x1c0cdf = _0x1c0cdf['\x73\x75\x62\x73\x74\x72\x69\x6e\x67'](_0x33c80e + 0x1);
        }
        var _0x1b3f48 = function s(_0x1c0cdf) {
            try {
                return _0xcbc80b['\x65\x76\x61\x6c']('\x28' + _0x1c0cdf + '\x29');
            } catch (_0x40b9c3) {
                return null;
            }
            // atob
        }(_0x1c0cdf = _0xcbc80b[_0x3a8e('0x2')](_0x1c0cdf));
        _0x1b3f48 && '\x6f\x62\x6a\x65\x63\x74' == typeof _0x1b3f48 && _0x1b3f48['\x64'] && (_0x1b3f48 = _0x1b3f48['\x64']);
        for (var _0x20b9fa = [], _0x10503c = 0x0, _0x1a524d = 0x0; _0x1a524d < _0x1b3f48['\x6c\x65\x6e\x67\x74\x68']; _0x1a524d++) {
            var _0x3641ed = _0x1b3f48['\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74'](_0x1a524d)
                , _0x341952 = _0x36ab38[_0x3a8e('0x3')](_0x10503c % _0x36ab38['\x6c\x65\x6e\x67\x74\x68']);
            _0x10503c += 0x1,
                _0x3641ed = 0x1 * _0x3641ed ^ _0x341952,
                _0x20b9fa[_0x3a8e('0x4')](_0x3641ed['\x74\x6f\x53\x74\x72\x69\x6e\x67'](0x2));
        }
        return function d(_0x1c0cdf) {
            for (var _0x36ab38 = [], _0x33c80e = 0x0; _0x33c80e < _0x1c0cdf['\x6c\x65\x6e\x67\x74\x68']; _0x33c80e++)
                _0x36ab38['\x70\x75\x73\x68'](_0xcbc80b['\x53\x74\x72\x69\x6e\x67']['\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65'](_0xcbc80b['\x70\x61\x72\x73\x65\x49\x6e\x74'](_0x1c0cdf[_0x33c80e], 0x2)));
            return _0x36ab38['\x6a\x6f\x69\x6e']('');
        }(_0x20b9fa);
    }
    ;
}(window);

console.log(window.decode_desc('@kJRfphusP9WadJoZ@eyJkIjogIkg4XHU3YjFiXHU3ZWMxUFlEQ3BcdTAwMTlcdTRlYzNcdTg4MmREXHU3MDIxTChIOFx1NTQyZlx1NGU0YlBDQERgXHUwMDE5XHU0ZjczXHU1YmQyRGFba1tpIFx1ODA3Nlx1NGUzNVx1NWVjZVVCYlx1MDAwZXdBXHU0ZjhhXHU3NDRjXHU1OTVlXHU4ZDdmS3tcdTZiNzNFXHUwMDAyXHU5NTUzXHU3MGM5XHU3YjNhXHU3ZWY3XHUwMDE5ZlNEalx1OTUxOVx1NWQxNlx1NWJmNlx1NzdiOXJcdTU5NGNcdTk2NDNcdTc3OWJcdTMwNzRTXHU3ZWYyXHU3M2EyXHU3NDBlQlx1MDAxNmkoeSxcdTgwNWFcdTUyYzlGW1pEUFx0XHUwMDE5dCZcdTliMzBcdTUyZDFPcVp6cT9TXHUwMDFhVlx1MDAxMGR9XHUwMDE1IFwiflx1NzIxNlx1NjUxMlx1ZmY3MWkxUjQqNDVkXHU2NWQ5XHU3ZWYwXHU1MjRhXHU5NjM0XHU1MjdjTFx1MDAwM0g4cSFcdTVmNzBcdThmYjhcdTViMjFcdTY1MDNcdWZmNGFcclx1NWIwM05QXHU1YjFlT3JcdTUzYTd+XHU1YjA2T1MxVlx1MDAwMXNuXHU1MjYxXHU5MDQxXHU4MDYxXHVmZjUwXHU2OGM5XHU1ZTIxXHUzMDA1XHU1ZTRmXHU1ZTU3XHU1ZTYzUzFWXHUwMDAxc2BcdTcxYzNcdTcwZGRcdTY1MmNcdTY3ZDZcdWZmNzV5XHUwMDE5aVx1MDAwYkVcdTAwMDJDRlx1OWIyN1x1NTJjYlx1MDAxYVx1MDAwZUFEIn0=@'));
