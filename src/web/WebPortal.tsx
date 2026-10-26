import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AppProvider } from './context/AppContext';
import { Layout } from './components/Layout';
import { HomePage } from './pages/HomePage';
import { CoursesPage } from './pages/CoursesPage';
import { NewsPage } from './pages/NewsPage';
import { VideosPage } from './pages/VideosPage';
import { ContactAboutPage } from './pages/ContactAboutPage';
import { LoginPage, LecturePage, ProfilePage, MessagePage } from './pages/UserPages';
import { AdminCpPage } from './pages/AdminCpPage';

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
            <Route path="/:lang" element={<HomePage />} />

            {/* Courses */}
            <Route path="/courses" element={<CoursesPage />} />
            <Route path="/courses/online" element={<CoursesPage />} />
            <Route path="/courses/:slug" element={<CoursesPage />} />
            <Route path="/:lang/courses" element={<CoursesPage />} />
            <Route path="/:lang/courses/online" element={<CoursesPage />} />
            <Route path="/:lang/courses/:slug" element={<CoursesPage />} />
            <Route path="/khoa-hoc" element={<CoursesPage />} />
            <Route path="/hoc-thu" element={<CoursesPage />} />
            <Route path="/dang-ky" element={<CoursesPage />} />
            <Route path="/promo" element={<CoursesPage />} />

            {/* Library / News */}
            <Route path="/news" element={<NewsPage mode="list" />} />
            <Route path="/news/index" element={<NewsPage mode="list" />} />
            <Route path="/news/category/:slug" element={<NewsPage mode="list" />} />
            <Route path="/news/view/:slug" element={<NewsPage mode="detail" />} />
            <Route path="/view/:slug" element={<NewsPage mode="detail" />} />
            <Route path="/:lang/news" element={<NewsPage mode="list" />} />
            <Route path="/:lang/news/index" element={<NewsPage mode="list" />} />
            <Route path="/:lang/news/:slug" element={<NewsPage mode="list" />} />
            <Route path="/:lang/news/view/:slug" element={<NewsPage mode="detail" />} />
            <Route path="/:lang/view/:slug" element={<NewsPage mode="detail" />} />

            {/* Videos Store */}
            <Route path="/videos" element={<VideosPage mode="cate" />} />
            <Route path="/videocate" element={<VideosPage mode="cate" />} />
            <Route path="/videocate.html" element={<VideosPage mode="cate" />} />
            <Route path="/videos/:cateSlug" element={<VideosPage mode="cate" />} />
            <Route path="/videocate/:cateSlug" element={<VideosPage mode="cate" />} />
            <Route path="/video/:cateSlug" element={<VideosPage mode="watch" />} />
            <Route path="/video/:cateSlug/:videoSlug" element={<VideosPage mode="watch" />} />
            <Route path="/:lang/videos" element={<VideosPage mode="cate" />} />
            <Route path="/:lang/videocate" element={<VideosPage mode="cate" />} />
            <Route path="/:lang/videocate/:cateSlug" element={<VideosPage mode="cate" />} />
            <Route path="/:lang/video/:cateSlug" element={<VideosPage mode="watch" />} />
            <Route path="/:lang/video/:cateSlug/:videoSlug" element={<VideosPage mode="watch" />} />

            {/* About, Opening Class, Sitemap, Contact */}
            <Route path="/about" element={<ContactAboutPage mode="about" />} />
            <Route path="/about/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/about-us" element={<ContactAboutPage mode="about" />} />
            <Route path="/about-us/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/opening" element={<ContactAboutPage mode="opening" />} />
            <Route path="/opening/:slug" element={<ContactAboutPage mode="opening" />} />
            <Route path="/sitemap" element={<ContactAboutPage mode="sitemap" />} />
            <Route path="/contact" element={<ContactAboutPage mode="contact" />} />
            <Route path="/:lang/about" element={<ContactAboutPage mode="about" />} />
            <Route path="/:lang/about/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/:lang/about-us" element={<ContactAboutPage mode="about" />} />
            <Route path="/:lang/about-us/:slug" element={<ContactAboutPage mode="about" />} />
            <Route path="/:lang/opening" element={<ContactAboutPage mode="opening" />} />
            <Route path="/:lang/opening/:slug" element={<ContactAboutPage mode="opening" />} />
            <Route path="/:lang/sitemap" element={<ContactAboutPage mode="sitemap" />} />
            <Route path="/:lang/contact" element={<ContactAboutPage mode="contact" />} />

            {/* Legacy Student & Trial Lectures */}
            <Route path="/user/login" element={<LoginPage />} />
            <Route path="/user/lecture" element={<LecturePage />} />
            <Route path="/user/lecture/:lectureSlug" element={<LecturePage />} />
            <Route path="/trial/:courseSlug" element={<LecturePage isTrial={true} />} />
            <Route path="/trial/:courseSlug/:lectureSlug" element={<LecturePage isTrial={true} />} />
            <Route path="/user/profile" element={<ProfilePage />} />
            <Route path="/user/message" element={<MessagePage />} />

            {/* AdminCP */}
            <Route path="/admincp" element={<AdminCpPage />} />

            {/* Fallback */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </AppProvider>
  );
}
