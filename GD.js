var eE = function (a) {
    a = a.split("");
    dE.gd(a, 31);
    dE.w7(a, 54);
    dE.gd(a, 3);
    dE.ev(a, 2);
    dE.w7(a, 24);
    dE.w7(a, 8);
    dE.ev(a, 1);
    dE.gd(a, 70);
    return a.join("");
};
var dE = {
    w7: function (a, b) {
        var c = a[0];
        a[0] = a[b % a.length];
        a[b % a.length] = c;
    },
    gd: function (a) {
        a.reverse();
    },
    ev: function (a, b) {
        a.splice(0, b);
    },
};
