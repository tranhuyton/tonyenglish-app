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
    const [currentTime, setCurrentTime] = useState('0:00');
    const [duration, setDuration] = useState('0:00');

    const formatTime = (time: number) => {
      if (isNaN(time) || !isFinite(time)) return '0:00';
      const minutes = Math.floor(time / 60);
      const seconds = Math.floor(time % 60);
      return `${minutes}:${seconds.toString().padStart(2, '0')}`;
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
        setCurrentTime('0:00');
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

    const handleSeek = (e: React.ChangeEvent<HTMLInputElement>) => {
      const audio = innerRef.current;
      if (!audio) return;

      const seekTime = (Number(e.target.value) / 100) * audio.duration;
      audio.currentTime = seekTime;
      setProgress(Number(e.target.value));
    };

    return (
      <div className={`flex items-center gap-3 bg-slate-100 rounded-full px-4 py-1.5 border border-slate-200 shadow-inner ${className}`}>
        <audio ref={innerRef} src={src} preload="auto" autoPlay={autoPlay} />
        
        <button 
          onClick={togglePlayPause}
          className="w-8 h-8 flex items-center justify-center bg-[#0ea5e9] text-white rounded-full hover:bg-[#0284c7] transition-colors shrink-0 shadow-sm"
        >
          {isPlaying ? (
            <span className="font-bold text-[10px]">⏸</span>
          ) : (
            <span className="font-bold text-[10px] ml-0.5">▶</span>
          )}
        </button>

        <div className="flex items-center gap-2 flex-1 min-w-[150px]">
          <span className="text-[12px] font-medium text-slate-500 font-mono w-9 text-right">{currentTime}</span>
          
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={progress} 
            onChange={handleSeek}
            className="flex-1 h-1.5 bg-slate-300 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:bg-[#0ea5e9] [&::-webkit-slider-thumb]:rounded-full"
          />
          
          <span className="text-[12px] font-medium text-slate-500 font-mono w-9">{duration}</span>
        </div>
      </div>
    );
  }
);

CustomAudioPlayer.displayName = 'CustomAudioPlayer';
