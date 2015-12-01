import download from './download';
import preprocess from './preprocess';

export function save(svgElement, config) {
  var defaultFileName = 'test';
  var filename = config.filename || defaultFileName;
  var svgInfo = preprocess(svgElement);
  download(svgInfo, filename);
}
