//g++ -std=c++17 5-Smallest-multiple.cpp
#include <numeric>
#include <iostream>

namespace math {

    template <typename M, typename N>
    constexpr auto lcm(const M& m, const N& n) {
        return std::lcm(m, n);
    }

    template <typename M, typename ...Rest>
    constexpr auto lcm(const M& first, const Rest&... rest) {
        return std::lcm(first, lcm(rest...));
    }
}

auto main() -> int {
  std::cout << math::lcm(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20) << std::endl;
    return 0;
}
