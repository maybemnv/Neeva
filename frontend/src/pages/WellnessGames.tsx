import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Play, Pause, Volume2, VolumeX, ArrowLeft, Wind, Sparkles } from 'lucide-react';
import { Link } from 'react-router-dom';

const FocusFlow = () => {
    const [isActive, setIsActive] = useState(false);
    const [phase, setPhase] = useState('Inhale'); // Inhale, Hold, Exhale, Hold
    const [, setCount] = useState(0);

    useEffect(() => {
        let interval: any;
        if (isActive) {
            interval = setInterval(() => {
                setCount((c) => {
                    const newCount = (c + 1) % 16;
                    if (newCount >= 0 && newCount < 4) setPhase('Inhale');
                    else if (newCount >= 4 && newCount < 8) setPhase('Hold');
                    else if (newCount >= 8 && newCount < 12) setPhase('Exhale');
                    else setPhase('Hold');
                    return newCount;
                });
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [isActive]);

    return (
        <div className="flex flex-col items-center justify-center h-[60vh]">
            <div className="relative flex items-center justify-center w-64 h-64">
                <motion.div
                    animate={{
                        scale: phase === 'Inhale' ? 1.5 : phase === 'Exhale' ? 1 : 1.5,
                        opacity: phase === 'Hold' ? 0.8 : 1,
                    }}
                    transition={{ duration: 4, ease: "easeInOut" }}
                    className="absolute inset-0 bg-gradient-to-br from-purple-500/30 to-blue-500/30 rounded-full blur-3xl"
                />
                <motion.div
                    animate={{
                        scale: phase === 'Inhale' ? 1.2 : phase === 'Exhale' ? 0.8 : 1.2,
                    }}
                    transition={{ duration: 4, ease: "easeInOut" }}
                    className="w-48 h-48 bg-white/10 backdrop-blur-md border border-white/20 rounded-full flex items-center justify-center shadow-2xl"
                >
                    <span className="text-2xl font-bold text-gray-800">{phase}</span>
                </motion.div>
            </div>
            <button
                onClick={() => setIsActive(!isActive)}
                className="mt-8 px-8 py-3 bg-gray-900 text-white rounded-full font-medium hover:bg-gray-800 transition-all shadow-lg shadow-purple-500/20 flex items-center gap-2"
            >
                {isActive ? <Pause size={20} /> : <Play size={20} />}
                {isActive ? 'Pause' : 'Start Focus'}
            </button>
        </div>
    );
};

const SensoryCalm = () => {
    const canvasRef = useRef<HTMLCanvasElement>(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        let particles: any[] = [];
        let animationFrameId: number;

        const resize = () => {
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        };
        window.addEventListener('resize', resize);
        resize();

        class Particle {
            x: number;
            y: number;
            size: number;
            speedX: number;
            speedY: number;
            color: string;

            constructor() {
                this.x = Math.random() * canvas!.width;
                this.y = Math.random() * canvas!.height;
                this.size = Math.random() * 5 + 1;
                this.speedX = Math.random() * 1 - 0.5;
                this.speedY = Math.random() * 1 - 0.5;
                this.color = `hsla(${Math.random() * 60 + 240}, 70%, 60%, ${Math.random() * 0.5})`;
            }

            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.size > 0.2) this.size -= 0.01;
                if (this.x < 0 || this.x > canvas!.width) this.speedX *= -1;
                if (this.y < 0 || this.y > canvas!.height) this.speedY *= -1;
            }

            draw() {
                ctx!.fillStyle = this.color;
                ctx!.beginPath();
                ctx!.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx!.fill();
            }
        }

        const init = () => {
            for (let i = 0; i < 50; i++) {
                particles.push(new Particle());
            }
        };

        const animate = () => {
            ctx!.clearRect(0, 0, canvas.width, canvas.height);
            if (particles.length < 100) {
                particles.push(new Particle());
            }
            for (let i = 0; i < particles.length; i++) {
                particles[i].update();
                particles[i].draw();
                if (particles[i].size <= 0.2) {
                    particles.splice(i, 1);
                    i--;
                }
            }
            animationFrameId = requestAnimationFrame(animate);
        };

        init();
        animate();

        return () => {
            window.removeEventListener('resize', resize);
            cancelAnimationFrame(animationFrameId);
        };
    }, []);

    return (
        <div className="w-full h-[60vh] bg-black/5 rounded-3xl overflow-hidden relative">
            <canvas ref={canvasRef} className="w-full h-full" />
            <div className="absolute bottom-6 left-1/2 -translate-x-1/2">
                <p className="text-gray-500 text-sm bg-white/80 backdrop-blur px-4 py-2 rounded-full">
                    Move your mouse to interact (Coming Soon)
                </p>
            </div>
        </div>
    );
};

const WellnessGames = () => {
    const [activeTab, setActiveTab] = useState<'focus' | 'sensory'>('focus');

    return (
        <div className="min-h-screen bg-[#FAFAFA] pb-20">
            <div className="max-w-6xl mx-auto p-6 md:p-8 space-y-8">
                {/* Header */}
                <div className="animate-in flex items-center gap-4">
                    <Link to="/wellness" className="p-2 hover:bg-gray-100 rounded-full transition-colors">
                        <ArrowLeft size={24} className="text-gray-600" />
                    </Link>
                    <div>
                        <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-2">Wellness Games</h1>
                        <p className="text-lg text-gray-600">Interactive experiences for focus and calm</p>
                    </div>
                </div>

                {/* Tabs */}
                <div className="flex gap-4 mb-8 animate-in">
                    <button
                        onClick={() => setActiveTab('focus')}
                        className={`flex items-center gap-2 px-6 py-3 rounded-2xl font-medium transition-all duration-300 ${activeTab === 'focus'
                                ? 'bg-gradient-to-r from-purple-600 to-blue-500 text-white shadow-lg shadow-purple-500/30'
                                : 'bg-white text-gray-600 hover:bg-gray-50'
                            }`}
                    >
                        <Wind size={20} />
                        Focus Flow
                    </button>
                    <button
                        onClick={() => setActiveTab('sensory')}
                        className={`flex items-center gap-2 px-6 py-3 rounded-2xl font-medium transition-all duration-300 ${activeTab === 'sensory'
                                ? 'bg-gradient-to-r from-purple-600 to-blue-500 text-white shadow-lg shadow-purple-500/30'
                                : 'bg-white text-gray-600 hover:bg-gray-50'
                            }`}
                    >
                        <Sparkles size={20} />
                        Sensory Calm
                    </button>
                </div>

                {/* Game Area */}
                <div className="bg-white rounded-[2.5rem] p-8 border border-gray-100 shadow-xl shadow-purple-500/5 animate-in">
                    <AnimatePresence mode="wait">
                        {activeTab === 'focus' ? (
                            <motion.div
                                key="focus"
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -20 }}
                            >
                                <div className="mb-6">
                                    <h2 className="text-2xl font-bold text-gray-900">Box Breathing</h2>
                                    <p className="text-gray-600">Follow the visual guide to regulate your breathing and improve focus.</p>
                                </div>
                                <FocusFlow />
                            </motion.div>
                        ) : (
                            <motion.div
                                key="sensory"
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -20 }}
                            >
                                <div className="mb-6">
                                    <h2 className="text-2xl font-bold text-gray-900">Particle Flow</h2>
                                    <p className="text-gray-600">Watch the soothing particles to calm your mind.</p>
                                </div>
                                <SensoryCalm />
                            </motion.div>
                        )}
                    </AnimatePresence>
                </div>
            </div>
        </div>
    );
};

export default WellnessGames;
