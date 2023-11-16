
function urlValues() {
    let keystring = window.location.search.substring(1);
    let keyarray = keystring.split('&');
    let keys = {};

    for (var i = 0; i < keyarray.length; i++) {
        let keypair = keyarray[i].split('=');
        let k1 = decodeURIComponent(keypair[0]);
        let k2 = decodeURIComponent(keypair[1]);
        keys[k1] = k2;

    }

    console.log(keys);
    return keys;
}

///?name=Youz&stuff=a
