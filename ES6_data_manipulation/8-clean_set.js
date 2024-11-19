export default function cleanSet(set, startString) {
  if (!set || !startString || typeof startString !== 'string' || startString === '') {
    return '';
  }

  return Array.from(set)
    .filter((value) => typeof value === 'string'
            && value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .filter((value) => value.length > 0)
    .join('-');
}
