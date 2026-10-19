export interface ClassConfig {
  cleanName: string;
  isTrial: boolean;
  trialLectureIds: string[];
}

const TRIAL_TAG_REGEX = /\s*\[trial(?::([^\]]*))?\]\s*$/i;

export function parseClassConfig(rawName?: string | null): ClassConfig {
  const str = (rawName || '').trim();
  const match = str.match(TRIAL_TAG_REGEX);
  if (!match) {
    return {
      cleanName: str,
      isTrial: false,
      trialLectureIds: [],
    };
  }
  const cleanName = str.replace(TRIAL_TAG_REGEX, '').trim() || 'Lớp học thử';
  const idsRaw = match[1] ? match[1].trim() : '';
  const trialLectureIds = idsRaw
    ? idsRaw.split(',').map(s => s.trim()).filter(Boolean)
    : [];
  return {
    cleanName,
    isTrial: true,
    trialLectureIds,
  };
}

export function formatClassConfig(
  cleanName: string,
  isTrial: boolean,
  trialLectureIds: string[] = []
): string {
  const clean = (cleanName || '').replace(TRIAL_TAG_REGEX, '').trim() || (isTrial ? 'Lớp học thử' : 'Lớp học');
  if (!isTrial) {
    return clean;
  }
  const uniqueIds = Array.from(new Set(trialLectureIds.map(s => s.trim()).filter(Boolean)));
  if (uniqueIds.length === 0) {
    return `${clean} [trial]`;
  }
  return `${clean} [trial:${uniqueIds.join(',')}]`;
}
