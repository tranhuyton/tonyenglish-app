export const TONYENGLISH_GTM_ID = 'GTM-TF5RJB35';
export const TONYENGLISH_GA4_ID = 'G-6CMFP5YQXM';
export const TONYENGLISH_META_PIXEL_ID = '1124721320167694';

declare global {
  interface Window {
    dataLayer?: any[];
    gtag?: (...args: any[]) => void;
    fbq?: (...args: any[]) => void;
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

export function trackMetaPixelEvent(
  eventName: string,
  params?: Record<string, any>,
  isCustom: boolean = false
) {
  if (typeof window === 'undefined') return;
  try {
    if (typeof window.fbq === 'function') {
      window.fbq(isCustom ? 'trackCustom' : 'track', eventName, {
        site_domain: 'tonyenglish.vn',
        ...(params || {}),
      });
    }
  } catch (err) {
    console.warn('[TonyEnglish Pixel] track error:', err);
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

/** Unified GA4 + Meta Pixel tracking helpers (prevent missed conversions outside CoursesPage) */
export function trackUnifiedContact(method: 'Zalo' | 'Phone' | 'Messenger', locationOrCourse: string) {
  trackTonyContact(method, locationOrCourse);
  trackMetaPixelEvent('Contact', {
    content_name: locationOrCourse,
    contact_method: method,
  });
}

export function trackUnifiedLead(
  source: string,
  courseOrContext: string,
  hasPhone: boolean = true
) {
  if (source === 'trial_modal') {
    trackTonySignUp(hasPhone, source);
    trackMetaPixelEvent('CompleteRegistration', {
      content_name: courseOrContext,
      lead_source: source,
      has_phone: hasPhone,
    });
  } else {
    trackTonyGa4Event('generate_lead', {
      lead_source: source,
      course_name: courseOrContext,
      has_phone: hasPhone,
    });
  }
  trackMetaPixelEvent('Lead', {
    content_name: courseOrContext,
    lead_source: source,
    has_phone: hasPhone,
  });
}

export function trackUnifiedViewCourse(courseName: string, courseId?: string) {
  trackTonyViewCourse(courseName, courseId);
  trackMetaPixelEvent('ViewContent', {
    content_name: courseName,
    content_ids: courseId ? [String(courseId)] : undefined,
    content_type: 'product',
    content_category: 'TonyEnglish_Courses',
  });
}
