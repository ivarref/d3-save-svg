export default function (svgInfo, filename) {

  var url = window.URL.createObjectURL(new Blob(svgInfo.source, {type: 'text\/xml'}));
  var body = document.body;
  var a = document.createElement('a');

  body.appendChild(a);
  a.setAttribute('download', filename + '.svg');
  a.setAttribute('href', url);
  a.style.display = 'none';
  a.click();

  setTimeout(function() {
    window.URL.revokeObjectURL(url);
  }, 10);
}
