const CryptoJS = require('crypto-js');

function getSign(city) {

    var currentTime = new Date();
    var year = currentTime.getFullYear();
    var mon = currentTime.getMonth() + 1;
    var day = currentTime.getDate();
    var hour = currentTime.getHours();
    var minute = currentTime.getMinutes();
    var second = currentTime.getSeconds();
    if (10 > day) {
        day = '0' + day;
    }
    if (10 > mon) {
        mon = '0' + mon;
    }
    if (10 > hour) {
        hour = '0' + hour;
    }
    if (10 > minute) {
        minute = '0' + minute;
    }
    if (10 > second) {
        second = '0' + second;
    }
    var timeString = year + '' + mon + '' + day + '' + hour + '' + minute + '' + second;
    var data = city + '_' + timeString;
    let key = CryptoJS.enc.Utf8.parse('5ha5Z7cZ3WNbD3rA');
    let iv = CryptoJS.enc.Utf8.parse('AYk98XaiBwCi0Dst');
    // 执行AES加密
    let encryptData = CryptoJS.AES.encrypt(data, key, {
        mode: CryptoJS.mode.CBC,
        iv: iv,
        padding: CryptoJS.pad.Pkcs7
    });
    
    return encryptData.toString();
}
