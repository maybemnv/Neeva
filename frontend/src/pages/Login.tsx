import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '@/contexts/AuthContext';
import { Sparkles, ArrowRight } from 'lucide-react';
import CircularText from '@/components/CircularText';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            await login(email, password);
            navigate('/');
        } catch (err: any) {
            setError(err.response?.data?.detail || 'Login failed. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center relative overflow-hidden bg-[#fdfbf7]">
            {/* Background Gradients */}
            <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
                <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] rounded-full bg-purple-200/30 blur-[100px] animate-float-slow" />
                <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] rounded-full bg-blue-200/30 blur-[100px] animate-float" />
            </div>

            {/* Rotating Text Decoration */}
            <div className="absolute top-10 left-10 hidden md:block opacity-20">
                <CircularText text="MENTAL WELLNESS • MINDFULNESS • BALANCE • " radius={80} />
            </div>

            <div className="w-full max-w-md relative z-10 p-4">
                {/* Logo */}
                <div className="text-center mb-10 animate-fade-in">
                    <div className="inline-flex items-center justify-center w-16 h-16 rounded-full gradient-purple mb-6 shadow-xl shadow-purple-200">
                        <Sparkles className="w-8 h-8 text-white" />
                    </div>
                    <h1 className="text-5xl font-serif font-bold text-gray-900 mb-3 tracking-tight">
                        Welcome back
                    </h1>
                    <p className="text-gray-500 font-medium">Your sanctuary awaits.</p>
                </div>

                {/* Login Card */}
                <div className="glass-strong rounded-[2.5rem] p-10 shadow-2xl animate-slide-up">
                    <form onSubmit={handleSubmit} className="space-y-6">
                        {error && (
                            <div className="bg-red-50 border border-red-100 text-red-600 px-4 py-3 rounded-2xl text-sm font-medium text-center">
                                {error}
                            </div>
                        )}

                        <div className="space-y-1">
                            <label className="block text-sm font-medium text-gray-600 ml-4">
                                Email
                            </label>
                            <input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="w-full px-6 py-4 bg-gray-50/50 border border-gray-200 rounded-full focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500 outline-none transition-all text-gray-900 placeholder-gray-400 hover:bg-white"
                                placeholder="hello@example.com"
                                required
                            />
                        </div>

                        <div className="space-y-1">
                            <label className="block text-sm font-medium text-gray-600 ml-4">
                                Password
                            </label>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="w-full px-6 py-4 bg-gray-50/50 border border-gray-200 rounded-full focus:ring-2 focus:ring-purple-500/20 focus:border-purple-500 outline-none transition-all text-gray-900 placeholder-gray-400 hover:bg-white"
                                placeholder="••••••••"
                                required
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full group relative overflow-hidden bg-gray-900 text-white py-4 rounded-full font-medium shadow-lg hover:shadow-xl hover:scale-[1.02] transition-all duration-300 disabled:opacity-70 disabled:cursor-not-allowed disabled:hover:scale-100"
                        >
                            <span className="relative z-10 flex items-center justify-center gap-2">
                                {loading ? 'Signing in...' : 'Sign in'}
                                {!loading && <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />}
                            </span>
                            <div className="absolute inset-0 bg-gradient-to-r from-purple-600 to-blue-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                        </button>
                    </form>

                    <div className="mt-8 text-center">
                        <p className="text-gray-500 text-sm">
                            New here?{' '}
                            <Link to="/register" className="text-gray-900 font-semibold hover:text-purple-600 transition-colors underline decoration-gray-300 underline-offset-4 hover:decoration-purple-600">
                                Create an account
                            </Link>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
