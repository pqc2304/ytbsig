var eE = function (a) {
    a = a.split("");
    gE.wF(a, 15);
    gE.kf(a, 36);
    gE.dx(a, 1);
    gE.wF(a, 66);
    gE.wF(a, 24);
    gE.dx(a, 2);
    return a.join("");
};
var gE = {
    kf: function (a) {
        a.reverse();
    },
    wF: function (a, b) {
        var c = a[0];
        a[0] = a[b % a.length];
        a[b % a.length] = c;
    },
    dx: function (a, b) {
        a.splice(0, b);
    },
};
