function() {
  for (e = arguments.length, t = Array(e), n = 0; n < e; n++) t[n] = arguments[n]
  var e, t, n, i = {
    target: s,
    args: t,
    label: "@glimmer/closure-action"
  }
  return (0, d.flaggedInstrument)("interaction.ember-action", i, (function() {
    return C.join.apply(void 0, [s, a].concat(r(t)))
  }))
}