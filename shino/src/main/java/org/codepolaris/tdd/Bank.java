package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;
import org.codepolaris.tdd.utils.Pair;

import java.util.HashMap;
import java.util.Map;

public class Bank {
  private Map<Pair, Integer> rates = new HashMap<>();

  public Money reduce(Expression source, String to) {
    return source.reduce(this, to);
  }

  void addRate(String from, String to, int rate) {
    rates.put(new Pair(from, to), rate);
  }

  int rate(String from, String to) {
    if (from.equals(to)) return 1;
    return rates.get(new Pair(from, to));
  }
}
