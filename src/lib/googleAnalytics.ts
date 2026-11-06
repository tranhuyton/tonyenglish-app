export const TONYENGLISH_GTM_ID = 'GTM-TF5RJB35';
export const TONYENGLISH_GA4_ID = 'G-6CMFP5YQXM';

declare global {
  interface Window {
    dataLayer?: any[];
    gtag?: (...args: any[]) => void;
  }
}

export function trackTonyGa4Event(eventName: string, params?: Record<string, any>) {
  if (typeof window === 'undefined') return;
  try {
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, params || {});
    } else if (Array.isArray(window.dataLayer)) {
      window.dataLayer.push(['event', eventName, params || {}]);
    }
  } catch (err) {
    console.warn('[TonyEnglish GA4] track error:', err);
  }
}

export function trackTonySignUp(hasPhone: boolean = false, source: string = 'trial_modal') {
  trackTonyGa4Event('sign_up', {
    method: 'email',
    has_phone: hasPhone,
    signup_source: source,
  });
  trackTonyGa4Event('generate_lead', {
    lead_source: source,
    has_phone: hasPhone,
  });
}

export function trackTonyVerifiedCallbackLead(courseName: string) {
  trackTonyGa4Event('generate_lead', {
    lead_source: 'callback_phone_form',
    course_name: courseName,
  });
}

export function trackTonyContact(method: 'Zalo' | 'Phone' | 'Messenger', courseOrLocation: string) {
  trackTonyGa4Event('contact_zalo_phone', {
    contact_channel: method.toLowerCase(),
    course_or_location: courseOrLocation,
  });
}

export function trackTonyViewCourse(courseName: string, courseId?: string) {
  trackTonyGa4Event('view_item', {
    items: [
      {
        item_id: courseId || courseName,
        item_name: courseName,
        item_category: 'TonyEnglish_IELTS_IGCSE',
      },
    ],
  });
}
