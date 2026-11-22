import React, { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate, Outlet } from 'react-router-dom';
import { AppProvider, useApp } from './context/AppContext';
import { Layout } from './components/Layout';
import { HomePage } from './pages/HomePage';
import { CoursesPage } from './pages/CoursesPage';
import { NewsPage } from './pages/NewsPage';
import { VideosPage } from './pages/VideosPage';
import { ContactAboutPage } from './pages/ContactAboutPage';
import { LoginPage, LecturePage, ProfilePage, MessagePage } from './pages/UserPages';

const LangRouteSync: React.FC<{ targetLang: 'vi' | 'en' }> = ({ targetLang }) => {
  const { setLang } = useApp();
  useEffect(() => {
    setLang(targetLang);
  }, [targetLang]);
  return <Outlet />;
};

export default function WebPortal({
  onNavigate,
}: {
  onNavigate?: (view: string) => void;
  onStartTest?: any;
}) {
  return (
    <AppProvider>
      <BrowserRouter>
        <Layout onNavigateLms={onNavigate}>
          <Routes>
            {/* Homepage */}
            <Route path="/" element={<HomePage />} />

            {/* Courses */}
            <Route path="/igcse" element={<Navigate to="/courses/luyen-thi-igcse-alevel-cap-toc" replace />} />
            <Route path="/courses" element={<CoursesPage />} />
            <Route path="/courses/online" element={<CoursesPage />} />
            <Route path="/courses/:slug" element={<CoursesPage />} />
            <Route path="/khoa-hoc" element={<CoursesPage />} />
            <Route path="/khoa-hoc/:slug" element={<CoursesPage />} />
            <Route path="/hoc-thu" element={<CoursesPage />} />
            <Route path="/dang-ky" element={<CoursesPage />} />
            <Route path="/promo" element={<CoursesPage />} />

            {/* Library / News */}
            <Route path="/news" element={<NewsPage mode="list" />} />
            <Route path="/news/index" element={<NewsPage mode="list" />} />
            <Route path="/news/category/:slug" element={<NewsPage mode="list" />} />
            <Route path="/news/view/:slug" element={<NewsPage mode="detail" />} />
            <Route path="/view/:slug" element={<NewsPage mode="detail" />} />

            {/* Videos Store */}
            <Route path="/videos" element={<VideosPage mode="cate" />} />
            <Route path="/videocate" element={<VideosPage mode="cate" />} />
            <Route path="/videocate.html" element={<VideosPage mode="cate" />} />
            <Route path="/videos/:cateSlug" element={<VideosPage mode="cate" />} />
            <Route path="/videocate/:cateSlug" element={<VideosPage mode="cate" />} />
            <Route path="/video/:cateSlug" element={<VideosPage mode="watch" />} />
            <Route path="/video/:cateSlug/:videoSlug" element={<VideosPage mode="watch" />} />

            {/* About, Opening Class, Sitemap, Contact */}
            <Route path="/about" element={<ContactAboutPage mode="about" />} />
            <Route path="/about/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/about-us" element={<ContactAboutPage mode="about" />} />
            <Route path="/about-us/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/opening" element={<ContactAboutPage mode="opening" />} />
            <Route path="/opening/:slug" element={<ContactAboutPage mode="opening" />} />
            <Route path="/sitemap" element={<ContactAboutPage mode="sitemap" />} />
            <Route path="/contact" element={<ContactAboutPage mode="contact" />} />

            {/* Explicit Localized Routes (/vi/* and /en/*) */}
            {(['vi', 'en'] as const).map((locale) => (
              <Route key={locale} path={`/${locale}`} element={<LangRouteSync targetLang={locale} />}>
                <Route index element={<HomePage />} />
                <Route path="igcse" element={<Navigate to="/courses/luyen-thi-igcse-alevel-cap-toc" replace />} />
                <Route path="courses" element={<CoursesPage />} />
                <Route path="courses/online" element={<CoursesPage />} />
                <Route path="courses/:slug" element={<CoursesPage />} />
                <Route path="news" element={<NewsPage mode="list" />} />
                <Route path="news/index" element={<NewsPage mode="list" />} />
                <Route path="news/category/:slug" element={<NewsPage mode="list" />} />
                <Route path="news/view/:slug" element={<NewsPage mode="detail" />} />
                <Route path="news/:slug" element={<NewsPage mode="list" />} />
                <Route path="view/:slug" element={<NewsPage mode="detail" />} />
                <Route path="videos" element={<VideosPage mode="cate" />} />
                <Route path="videos/:cateSlug" element={<VideosPage mode="cate" />} />
                <Route path="videocate" element={<VideosPage mode="cate" />} />
                <Route path="videocate/:cateSlug" element={<VideosPage mode="cate" />} />
                <Route path="video/:cateSlug" element={<VideosPage mode="watch" />} />
                <Route path="video/:cateSlug/:videoSlug" element={<VideosPage mode="watch" />} />
                <Route path="about" element={<ContactAboutPage mode="about" />} />
                <Route path="about/:slug" element={<ContactAboutPage mode="about" />} />
                <Route path="about-us" element={<ContactAboutPage mode="about" />} />
                <Route path="about-us/:slug" element={<ContactAboutPage mode="about" />} />
                <Route path="opening" element={<ContactAboutPage mode="opening" />} />
                <Route path="opening/:slug" element={<ContactAboutPage mode="opening" />} />
                <Route path="sitemap" element={<ContactAboutPage mode="sitemap" />} />
                <Route path="contact" element={<ContactAboutPage mode="contact" />} />
              </Route>
            ))}

            {/* Legacy Student & Trial Lectures */}
            <Route path="/user/login" element={<LoginPage />} />
            <Route path="/user/lecture" element={<LecturePage />} />
            <Route path="/user/lecture/:lectureSlug" element={<LecturePage />} />
            <Route path="/trial/:courseSlug" element={<LecturePage isTrial={true} />} />
            <Route path="/trial/:courseSlug/:lectureSlug" element={<LecturePage isTrial={true} />} />
            <Route path="/user/profile" element={<ProfilePage />} />
            <Route path="/user/message" element={<MessagePage />} />

            {/* Legacy AdminCP removed — redirect to homepage */}
            <Route path="/admincp" element={<Navigate to="/" replace />} />
            <Route path="/admincp/*" element={<Navigate to="/" replace />} />

            {/* Fallback */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </AppProvider>
  );
}
