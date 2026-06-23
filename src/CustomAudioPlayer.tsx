import React, { useState, useEffect, forwardRef, useImperativeHandle, useRef } from 'react';

interface CustomAudioPlayerProps {
  src: string;
  className?: string;
  autoPlay?: boolean;
}

export const CustomAudioPlayer = forwardRef<HTMLAudioElement, CustomAudioPlayerProps>(
  ({ src, className = '', autoPlay = false }, ref) => {
    const innerRef = useRef<HTMLAudioElement>(null);
    useImperativeHandle(ref, () => innerRef.current as HTMLAudioElement);

    const [isPlaying, setIsPlaying] = useState(false);
    const [progress, setProgress] = useState(0);
    const [currentTime, setCurrentTime] = useState('00:00');
    const [duration, setDuration] = useState('00:00');
    const [isMuted, setIsMuted] = useState(false);

    const formatTime = (time: number) => {
      if (isNaN(time) || !isFinite(time)) return '00:00';
      const minutes = Math.floor(time / 60);
      const seconds = Math.floor(time % 60);
      return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    };

    useEffect(() => {
      const audio = innerRef.current;
      if (!audio) return;

      const updateProgress = () => {
        setCurrentTime(formatTime(audio.currentTime));
        setProgress((audio.currentTime / audio.duration) * 100 || 0);
      };

      const handleLoadedMetadata = () => {
        setDuration(formatTime(audio.duration));
      };

      const handleEnded = () => {
        setIsPlaying(false);
        setProgress(0);
        setCurrentTime('00:00');
      };

      const handlePlay = () => setIsPlaying(true);
      const handlePause = () => setIsPlaying(false);

      audio.addEventListener('timeupdate', updateProgress);
      audio.addEventListener('loadedmetadata', handleLoadedMetadata);
      audio.addEventListener('ended', handleEnded);
      audio.addEventListener('play', handlePlay);
      audio.addEventListener('pause', handlePause);

      return () => {
        audio.removeEventListener('timeupdate', updateProgress);
        audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
        audio.removeEventListener('ended', handleEnded);
        audio.removeEventListener('play', handlePlay);
        audio.removeEventListener('pause', handlePause);
      };
    }, []);

    const togglePlayPause = () => {
      const audio = innerRef.current;
      if (!audio) return;

      if (isPlaying) {
        audio.pause();
      } else {
        audio.play();
      }
    };

    const skip = (seconds: number) => {
      const audio = innerRef.current;
      if (!audio) return;
      audio.currentTime = Math.max(0, Math.min(audio.currentTime + seconds, audio.duration || 0));
    };

    const toggleMute = () => {
      const audio = innerRef.current;
      if (!audio) return;
      audio.muted = !isMuted;
      setIsMuted(!isMuted);
    };

    const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
      const audio = innerRef.current;
      if (!audio) return;

      const seekTime = (Number(e.target.value) / 100) * audio.duration;
      audio.currentTime = seekTime;
      setProgress(Number(e.target.value));
    };

    return (
      <div className={`flex items-center gap-4 bg-slate-50 rounded-xl px-5 py-3 border border-slate-200 shadow-sm ${className}`}>
        <audio ref={innerRef} src={src} preload="auto" autoPlay={autoPlay} />
        
        {/* Playback Controls */}
        <div className="flex items-center gap-3 shrink-0 text-[#0ea5e9]">
          <button onClick={() => skip(-15)} className="hover:opacity-70 transition" title="Lùi 15s">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
                <path d="M3 3v5h5"/>
                <text x="12" y="16" fontSize="8" fill="currentColor" stroke="none" textAnchor="middle">15</text>
            </svg>
          </button>
          
          <button onClick={togglePlayPause} className="hover:opacity-70 transition">
            {isPlaying ? (
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-8 h-8">
                <path fillRule="evenodd" d="M6.75 5.25a.75.75 0 01.75-.75H9a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H7.5a.75.75 0 01-.75-.75V5.25zm7.5 0A.75.75 0 0115 4.5h1.5a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H15a.75.75 0 01-.75-.75V5.25z" clipRule="evenodd" />
              </svg>
            ) : (
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-8 h-8">
                <path fillRule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clipRule="evenodd" />
              </svg>
            )}
          </button>

          <button onClick={() => skip(15)} className="hover:opacity-70 transition" title="Tiến 15s">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21 12a9 9 0 1 1-9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/>
                <path d="M21 3v5h-5"/>
                <text x="12" y="16" fontSize="8" fill="currentColor" stroke="none" textAnchor="middle">15</text>
            </svg>
          </button>
        </div>

        {/* Time and Progress */}
        <div className="flex items-center gap-3 flex-1 min-w-[150px]">
          <span className="text-[13px] font-semibold text-slate-600 font-mono tracking-wider shrink-0">
            {currentTime} / {duration}
          </span>
          
          <div className="relative flex-1 h-1.5 flex items-center">
            <input 
              type="range" 
              min="0" 
              max="100" 
              value={progress} 
              onChange={handleSeek}
              className="absolute w-full h-1.5 opacity-0 cursor-pointer z-10"
            />
            <div className="w-full h-1.5 bg-slate-200 rounded-full overflow-hidden">
                <div className="h-full bg-[#0ea5e9] transition-all duration-100 ease-linear" style={{ width: `${progress}%` }}></div>
            </div>
            <div 
                className="absolute h-3 w-3 bg-[#0ea5e9] rounded-full shadow pointer-events-none transform -translate-x-1/2" 
                style={{ left: `${progress}%` }}
            ></div>
          </div>
        </div>

        {/* Volume */}
        <button onClick={toggleMute} className="text-slate-500 hover:text-slate-700 transition shrink-0 ml-2" title="Âm lượng">
          {isMuted ? (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
              <path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 001.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06zM17.78 9.22a.75.75 0 10-1.06 1.06L18.44 12l-1.72 1.72a.75.75 0 001.06 1.06l1.72-1.72 1.72 1.72a.75.75 0 101.06-1.06L20.56 12l1.72-1.72a.75.75 0 00-1.06-1.06l-1.72 1.72-1.72-1.72z" />
            </svg>
          ) : (
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-5 h-5">
              <path d="M13.5 4.06c0-1.336-1.616-2.005-2.56-1.06l-4.5 4.5H4.508c-1.141 0-2.318.664-2.66 1.905A9.76 9.76 0 001.5 12c0 .898.121 1.768.35 2.595.341 1.24 1.518 1.905 2.659 1.905h1.93l4.5 4.5c.945.945 2.561.276 2.561-1.06V4.06zM18.584 5.106a.75.75 0 011.06 0c3.808 3.807 3.808 9.98 0 13.788a.75.75 0 11-1.06-1.06 8.25 8.25 0 000-11.668.75.75 0 010-1.06z" />
              <path d="M15.932 7.757a.75.75 0 011.061 0 6 6 0 010 8.486.75.75 0 01-1.06-1.061 4.5 4.5 0 000-6.364.75.75 0 010-1.06z" />
            </svg>
          )}
        </button>
      </div>
    );
  }
);

CustomAudioPlayer.displayName = 'CustomAudioPlayer';
